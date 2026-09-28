# 会计账簿更新记录-gl_book_version

## 会计账簿更新记录-主表 t_gl_book_version

- **表名称：** 会计账簿更新记录-主表
- **表名：** t_gl_book_version

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyearprofitacctid | 新本年利润科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 3 | foldyearacctid | 旧本年利润科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 4 | fdisableperiodid | 失效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | foldaccttabid | 旧科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 7 | fenabledate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 8 | fdisabledate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fenableperiodid | 生效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 10 | faccounttableid | 新科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 11 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 12 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 13 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_book_version |  | forgid,fbooktypeid,fenableperiodid |
| 2 | pk_t_gl_book_version |  | fid |
