# 苍穹星瀚微服务收集-pbd_mserviceconfig

## 苍穹星瀚微服务收集-主表 t_pbd_mserviceconfig

- **表名称：** 苍穹星瀚微服务收集-主表
- **表名：** t_pbd_mserviceconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 微服务方法标识 | varchar | 512 |  | √ | ' ' | 微服务方法标识 |
| 3 | fmservicedesc | 微服务实现描述 | varchar | 512 |  | √ | ' ' | 微服务实现描述 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbizcloudid | 业务云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 8 | fnumber | 微服务定义标识 | varchar | 80 |  | √ | ' ' | 微服务定义标识 |
| 9 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_mserviceconfig |  | fid |
| 2 | idx_pbd_mserviceconfig_fnumber |  | fnumber,fbizcloudid,fbizappid,fname |
