# 历史打开期间-gl_openedperiod

## 历史打开期间-主表 t_gl_openedperiod

- **表名称：** 历史打开期间-主表
- **表名：** t_gl_openedperiod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 3 | fperiodid | 打开期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_openedperiod |  | fid |
| 2 | idx_gl_openedperiod |  | forgid,fbooktypeid |
