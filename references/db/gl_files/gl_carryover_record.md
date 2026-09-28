# 余额结转记录-gl_carryover_record

## 余额结转记录-主表 t_gl_carryover_record

- **表名称：** 余额结转记录-主表
- **表名：** t_gl_carryover_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 3 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 |
| 4 | fvoucherentryid | 凭证分录id | int8 | 64 |  | √ | 0 | 凭证分录id |
| 5 | fassgrpid | 维度 | int8 | 64 |  | √ | 0 | 维度 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 |
| 8 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币别 |
| 10 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 科目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_carryover_record_fvchid |  | fvoucherid |
| 2 | idx_gl_carryover_record_fbal |  | forgid,fbooktypeid,faccountid,fassgrpid,fcurrencyid,fmeasureunitid |
| 3 | pk_t_gl_carryover_record |  | fid |
| 4 | idx_gl_carryover_record_fentid |  | fvoucherentryid |
