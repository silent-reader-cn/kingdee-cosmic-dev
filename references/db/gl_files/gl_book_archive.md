# 账簿归档-gl_book_archive

## 账簿归档-主表 t_gl_bookarchive

- **表名称：** 账簿归档-主表
- **表名：** t_gl_bookarchive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchivetype | 归档类型 | varchar | 50 |  | √ | ' ' | 归档类型,枚举: gl_accountbook :账簿 gl_voucher :凭证 gl_rpt_generalledger :总分类账 gl_rpt_subledger :明细分类账 |
| 3 | fperiodid | 归档期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | farchivestatus | 归档状态 | bpchar | 1 |  | √ | '0' | 归档状态,枚举: 0 :未归档 1 :已归档 |
| 5 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 6 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_bookarchive |  | fid |
| 2 | idx_gl_bookarchive_bookid |  | fbookid,fperiodid |
