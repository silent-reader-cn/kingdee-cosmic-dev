# 单据重算节点信息-im_bal_recal_point

## 单据重算节点信息-主表 t_im_bal_recal_point

- **表名称：** 单据重算节点信息-主表
- **表名：** t_im_bal_recal_point

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fendid | 单据截止ID | int8 | 64 |  | √ | 0 | 单据截止ID |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | 'B' | 状态,枚举: A :已确认 B :待处理 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fruleid | 余额规则 | varchar | 30 |  | √ | ' ' | 余额更新规则列表 bal_balanceupdaterule |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_bal_recal_point |  | fid |
| 2 | idx_im_recal_rule |  | fruleid |
