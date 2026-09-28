# 车船税税源明细表（船舶）-totf_tcvvt_shipsdetail

## 车船税税源明细表（船舶）-主表 t_totf_tcvvt_shipsdetail

- **表名称：** 车船税税源明细表（船舶）-主表
- **表名：** t_totf_tcvvt_shipsdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhosttype | 主机种类 | varchar | 50 |  | √ | ' ' | 主机种类 |
| 3 | fsbcbzs | 申报船舶总数（艘） | int4 | 32 |  | √ | 0 | 申报船舶总数（艘） |
| 4 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 5 | fidennumber | 船舶识别号 | varchar | 50 |  | √ | ' ' | 船舶识别号 |
| 6 | fenginepower | 主机功率 | varchar | 50 |  | √ | ' ' | 主机功率 |
| 7 | fissuedate | 发证日期 | timestamp | 0 |  |  | null | 发证日期 |
| 8 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 9 | fhomeport | 船籍港 | varchar | 50 |  | √ | ' ' | 船籍港 |
| 10 | fshipname | 中文船名 | varchar | 200 |  | √ | ' ' | 中文船名 |
| 11 | fhulllength | 艇身长度(总长) | varchar | 50 |  | √ | ' ' | 艇身长度(总长) |
| 12 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 13 | fownershipdate | 取得所有权日期 | timestamp | 0 |  |  | null | 取得所有权日期 |
| 14 | fnettonnage | 净吨位 | numeric | 23 | 10 | √ | 0 | 净吨位 |
| 15 | fregnumber | 船舶登记号 | varchar | 50 |  | √ | ' ' | 船舶登记号 |
| 16 | fcompletiondate | 建成日期 | timestamp | 0 |  |  | null | 建成日期 |
| 17 | fshiptype | 船舶种类 | varchar | 50 |  | √ | ' ' | 船舶种类 |
| 18 | finiregnumber | 初次登记号码 | varchar | 50 |  | √ | ' ' | 初次登记号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_tcvvt_shipsdetail |  | fsbbid,fewblxh |
| 2 | pk_totf_tcvvt_shipsdetail |  | fid |
