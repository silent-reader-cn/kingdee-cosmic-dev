# 领域云（规则引擎）-plm_rengine_cloud

## 领域云（规则引擎）-主表 t_plm_egn_cloud

- **表名称：** 领域云（规则引擎）-主表
- **表名：** t_plm_egn_cloud

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcloudid | 云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 6 | findex | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |
| 7 | finitdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工录入 1 :初始化 |
| 8 | finitstatus | 初始化状态 | varchar | 50 |  | √ | ' ' | 初始化状态,枚举: 0 :进行中 1 :已验证 2 :已完成 |
| 9 | finitbatch | 初始化批次 | int8 | 64 |  | √ | 0 | 初始化批次 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_egn_cloud |  | fid |
| 2 | idx_plm_egn_cloud |  | fcloudid |
