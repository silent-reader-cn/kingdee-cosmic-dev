# 单据异常历史记录-task_exceptionhistory

## 单据异常历史记录-主表 t_tk_excphistory

- **表名称：** 单据异常历史记录-主表
- **表名：** t_tk_excphistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcompensatestatus | 处理状态 | varchar | 10 |  | √ | ' ' | 处理状态,枚举: 0 :失败 1 :成功 2 :标过 3 :停止 |
| 4 | fretrytime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 5 | ffailuretime | 异常创建时间 | timestamp | 0 |  |  | null | 异常创建时间 |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | frequestparam | 请求参数 | varchar | 210 |  | √ | ' ' | 请求参数 |
| 10 | frequestparam_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | ffailurereason_tag | 异常原因_详情 | text | 0 |  |  | null | 异常原因_详情 |
| 13 | fdealtype | 处理方式 | varchar | 10 |  | √ | ' ' | 处理方式 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fexceptiontype | 异常类型 | varchar | 25 |  | √ | ' ' | 异常类型 |
| 16 | fbillid | 单据id | varchar | 100 |  | √ | ' ' | 单据id |
| 17 | ffailurereason | 异常原因 | varchar | 210 |  | √ | ' ' | 异常原因 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_excphistory_pkey |  | fid |
| 2 | idx_ssc_excephis_fbillno |  | fbillno |
