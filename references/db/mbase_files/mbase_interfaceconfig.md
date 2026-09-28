# 业务接口配置-mbase_interfaceconfig

## 业务接口配置-主表 t_mbase_interfaceconfig

- **表名称：** 业务接口配置-主表
- **表名：** t_mbase_interfaceconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 接口名称 | varchar | 50 |  | √ | ' ' | 接口名称 |
| 4 | fmethodname | methodName | varchar | 50 |  | √ | ' ' | methodName |
| 5 | ftype | 接口类型 | bpchar | 1 |  | √ | '1' | 接口类型,枚举: 0 :定时消息服务 |
| 6 | fcloudid | cloudId | varchar | 30 |  | √ | ' ' | cloudId |
| 7 | fservicename | serviceName | varchar | 30 |  | √ | ' ' | serviceName |
| 8 | fway | 调用方式 | bpchar | 1 |  | √ | '0' | 调用方式,枚举: 0 :微服务 |
| 9 | fenable | 数据状态 | bpchar | 1 |  | √ | '1' | 数据状态,枚举: 0 :禁用 1 :可用 |
| 10 | fdesc | 接口说明 | varchar | 1000 |  | √ | ' ' | 接口说明 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fappid | appId | varchar | 30 |  | √ | ' ' | appId |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mbase_interfaceconfig |  | fid |
| 2 | idx_mbase_infterfaceconfig_fna |  | fname |
