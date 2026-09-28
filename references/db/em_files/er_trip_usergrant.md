# 用户授权信息-er_trip_usergrant

## 用户授权信息-主表 t_er_trip_usergrant

- **表名称：** 用户授权信息-主表
- **表名：** t_er_trip_usergrant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgrantip | 授权IP | varchar | 255 |  | √ | ' ' | 授权IP |
| 3 | fgrantcontent_tag | 授权内容_详情 | text | 0 |  | √ | ' ' | 授权内容_详情 |
| 4 | fgrantcontent | 授权内容 | varchar | 255 |  | √ | ' ' | 授权内容 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 |
| 6 | fgrantservers | 授权服务商 | varchar | 255 |  | √ | ' ' | 授权服务商,枚举: MEITUAN :美团 DIDI :滴滴 CHAILVYIHAO :差旅壹号 XIECHENG :携程 GAODE :高德 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 MEITUAN_NEW :美团商企通 |
| 7 | fgrantmodel | 授权设备 | varchar | 50 |  | √ | ' ' | 授权设备 |
| 8 | fgrant | 已授权 | bpchar | 1 |  | √ | '0' | 已授权,枚举: 1 :是 0 :否 |
| 9 | fgrantuser | 授权用户 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fgrantuserno | 授权人工号 | varchar | 50 |  | √ | ' ' | 授权人工号 |
| 11 | fgrantusername | 授权人姓名 | varchar | 50 |  | √ | ' ' | 授权人姓名 |
| 12 | fgranttime | 授权日期 | timestamp | 0 |  |  | null | 授权日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_usergrant_userno |  | fgrantuserno,fgrantusername |
| 2 | pk_er_usergrant |  | fid |
