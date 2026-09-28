# 差异结转规则-sca_diffrule

## 差异结转规则-主表 t_sca_diffrule

- **表名称：** 差异结转规则-主表
- **表名：** t_sca_diffrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | frate | 结转比例 | numeric | 23 | 10 | √ | 0.0000000000 | 结转比例 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcarryoverbill | 参与结转单据 | varchar | 255 |  | √ | ' ' | 参与结转单据,枚举: UNABSORBDIFF :未吸收差异单 FINISHDIFFBILL :完工结算差异单 |
| 8 | fdiffrule | 差异结转规则 | varchar | 255 |  | √ | ' ' | 差异结转规则,枚举: MANUAL :手工录入 PRODINPUTAMT :产品出库金额/（期初库存余额+本期入库金额） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_diffrule |  | forgid,fcostcenterid |
| 2 | t_sca_diffrule_pkey |  | fid |
