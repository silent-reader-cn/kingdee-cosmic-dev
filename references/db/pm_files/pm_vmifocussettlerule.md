# VMI集中结算规则-pm_vmifocussettlerule

## VMI集中结算规则-主表 t_pm_vmifocussettlerule

- **表名称：** VMI集中结算规则-主表
- **表名：** t_pm_vmifocussettlerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | frqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_vmifocussettlerule_mat |  | forgid,frqorgid,fmaterialid |
| 2 | idx_pm_vmifocussettlerule_num |  | fnumber |
| 3 | pk_t_pm_vmifocussettlerule |  | fid |
