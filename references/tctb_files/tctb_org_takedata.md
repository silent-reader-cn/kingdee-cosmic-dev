# 组织取数-tctb_org_takedata

## 组织取数-主表 t_tctb_org_takedata

- **表名称：** 组织取数-主表
- **表名：** t_tctb_org_takedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fenddate | 取数有效期止 | timestamp | 0 |  |  | null | 取数有效期止 |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fstartdate | 取数有效期起 | timestamp | 0 |  |  | null | 取数有效期起 |
| 6 | fcmborgtype | 职能类型 | int8 | 64 |  | √ | 0 | 组织职能类型 bos_org_biz |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_org_takedata |  | ftaxorg |
| 2 | pk_tctb_org_takedata |  | fid |
