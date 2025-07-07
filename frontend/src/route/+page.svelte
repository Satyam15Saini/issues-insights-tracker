<script>
  import { onMount } from 'svelte';
  let issues = [];
  let loading = true;

  onMount(async () => {
    try {
      const res = await fetch("http://localhost:8000/api/issues");
      issues = await res.json();
    } catch (err) {
      console.error("Failed to load issues:", err);
    } finally {
      loading = false;
    }
  });
</script>

<h1 class="text-3xl font-bold mb-4">Issues Dashboard</h1>

{#if loading}
  <p class="text-gray-500">Loading...</p>
{:else if issues.length === 0}
  <p class="text-gray-500">No issues found.</p>
{:else}
  <div class="overflow-x-auto">
    <table class="min-w-full bg-white border rounded shadow">
      <thead>
        <tr class="bg-gray-200 text-left">
          <th class="py-2 px-4">Title</th>
          <th class="py-2 px-4">Severity</th>
          <th class="py-2 px-4">Status</th>
        </tr>
      </thead>
      <tbody>
        {#each issues as issue}
          <tr class="border-t">
            <td class="py-2 px-4">{issue.title}</td>
            <td class="py-2 px-4">{issue.severity}</td>
            <td class="py-2 px-4">{issue.status}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
{/if}
