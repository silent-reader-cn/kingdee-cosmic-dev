# 地图服务-bos_mapservice_config

## 地图服务-主表 t_bos_mapservice_config

- **表名称：** 地图服务-主表
- **表名：** t_bos_mapservice_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmapservice | 地图服务 | varchar | 50 |  | √ | ' ' | 地图服务,枚举: default :默认 amap :高德地图 baidumap :百度地图 |
| 6 | fbaidu_serverkey | 服务端密钥 | varchar | 512 |  | √ | ' ' | 服务端密钥 |
| 7 | fiscustomservice | fiscustomservice | bpchar | 1 |  | √ | '0' |  |
| 8 | famap_apikey | Web服务API密钥 | varchar | 512 |  | √ | ' ' | Web服务API密钥 |
| 9 | famap_securitykey | 安全密钥 | varchar | 512 |  | √ | ' ' | 安全密钥 |
| 10 | famap_jsapikey | Web端(JS API)密钥 | varchar | 512 |  | √ | ' ' | Web端(JS API)密钥 |
| 11 | fbaidu_browserkey | 浏览器端密钥 | varchar | 512 |  | √ | ' ' | 浏览器端密钥 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bos_mapservice_config |  | fid |
