javascript:(function(){
  const target = encodeURIComponent(location.href);
  const proxy = 'https://corsproxy.io/?' + target;
  window.open(proxy, '_blank');
})();
