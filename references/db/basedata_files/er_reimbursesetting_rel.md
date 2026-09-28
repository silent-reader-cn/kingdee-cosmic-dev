# 报销级别设置关联表-er_reimbursesetting_rel

## 报销级别设置关联表-主表 t_er_reimbursesetting_rel

- **表名称：** 报销级别设置关联表-主表
- **表名：** t_er_reimbursesetting_rel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 3 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcompany | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_reimbursesetting_rel |  | fid |
| 2 | idx_er_companyuser |  | fuser,fcompany |
