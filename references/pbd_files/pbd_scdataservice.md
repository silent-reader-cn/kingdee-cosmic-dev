# 协同数据处理服务注册-pbd_scdataservice

## 协同数据处理服务注册-主表 t_pur_scdataservice

- **表名称：** 协同数据处理服务注册-主表
- **表名：** t_pur_scdataservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 服务描述 | varchar | 255 |  | √ | ' ' | 服务描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisv | 开发商 | varchar | 255 |  | √ | ' ' | 开发商 |
| 6 | fservicetype | 服务执行类型 | varchar | 50 |  | √ | ' ' | 服务执行类型,枚举: storedata :数据存储 pushdata :数据请求 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fserviceclass | 服务处理类 | varchar | 255 |  | √ | ' ' | 服务处理类 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | fentityid | 处理实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 14 | fhandleproperty | 处理属性 | varchar | 120 |  | √ | ' ' | 处理属性,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_sds_fnumber |  | fnumber |
| 2 | pk_t_pur_scdataservice |  | fid |
