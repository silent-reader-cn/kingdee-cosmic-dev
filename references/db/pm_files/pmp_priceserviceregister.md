# 价控服务注册-pmp_priceserviceregister

## 价控服务注册-主表 t_msbd_priceservregister

- **表名称：** 价控服务注册-主表
- **表名：** t_msbd_priceservregister

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fservice | 业务服务 | varchar | 5 |  | √ | ' ' | 业务服务,枚举: sctl :销售限价服务 pctl :采购限价服务 |
| 3 | fbizentity | 业务单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fcontrolpoint | 控制时点 | varchar | 500 |  |  | null | 控制时点,枚举: submit :提交 audit :审核 |
| 6 | forgsign | 限价组织 | varchar | 50 |  | √ | ' ' | 限价组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_serr_fbizentity |  | fbizentity |
| 2 | pk_t_msbd_priceservregister |  | fid |
