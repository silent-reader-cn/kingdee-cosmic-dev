# 协同数据转换配置-pbd_transferconfig

## 协同数据转换配置-主表 t_pbd_transferconfig

- **表名称：** 协同数据转换配置-主表
- **表名：** t_pbd_transferconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 数据转换描述 | varchar | 255 |  | √ | ' ' | 数据转换描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftransferkey | 数据转换标识 | varchar | 120 |  |  | ' ' | 数据转换标识 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftransferschemeid | 数据集成对象 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |
| 7 | fbizextpluginid | 业务扩展插件 | int8 | 64 |  | √ | '0' | 绑定业务插件 bos_bizextpluginbind |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftransferbotpid | 单据转换数据 | varchar | 36 |  | √ | ' ' | 转换规则 botp_crlist |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ftransfertype | 数据转换类型 | varchar | 50 |  | √ | ' ' | 数据转换类型,枚举: botptransfer :单据转换框架 iscschemetransfer :数据集成转换 sdktransfer :苍穹平台SDK |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pbd_stc_transferkey |  | ftransferkey |
| 2 | idx_t_pbd_stc_fname |  | fname |
| 3 | pk_t_pbd_transferconfig |  | fid |
