# 凭证归档数据-gl_filingdata

## 凭证归档数据-主表 t_gl_filingdata

- **表名称：** 凭证归档数据-主表
- **表名：** t_gl_filingdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ffilingstatus | 归档状态 | bpchar | 1 |  | √ | '1' | 归档状态,枚举: 1 :已归档 2 :未归档 |
| 5 | ffilingpersonid | 归档人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 7 | fscanpersonid | 扫描人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 9 | fsendvoucherid | 通知单凭证id | int8 | 64 |  | √ | 0 | 通知单凭证id |
| 10 | fbilltypeid | 单据类型 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_filingdata_creatime |  | fcreatetime |
| 2 | idx_gl_filingdata_fvoucherid |  | fvoucherid |
| 3 | t_gl_filingdata_pkey |  | fid |
