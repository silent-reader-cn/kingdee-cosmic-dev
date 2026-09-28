# 合同签订-er_contractsign

## 签约方分录-子表 t_er_consignparty

- **表名称：** 签约方分录-子表
- **表名：** t_er_consignparty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontractparty | 签约方名称 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | fpartperson | 签约人 | varchar | 80 |  | √ | ' ' | 签约人 |
| 4 | ftaxcertificate | 纳税人资质 | varchar | 200 |  | √ | ' ' | 纳税人资质 |
| 5 | fpartytype | 签约方类型 | varchar | 50 |  | √ | ' ' | 签约方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 |
| 6 | fsigntel | 联系电话 | varchar | 255 |  | √ | ' ' | 联系电话 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcontactperson | 联系人 | varchar | 100 |  | √ | ' ' | 联系人 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fsigncontract | 签约方 | varchar | 50 |  | √ | ' ' | 签约方,枚举: 0 :甲方 1 :乙方 2 :其他方 |
| 11 | fpartysrcentryid | 源单分录di | int8 | 64 |  | √ | 0 | 源单分录di |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_consignparty |  | fentryid |
| 2 | idx_er_signcontparty_seq |  | fid,fseq |

---

## 合同签订-主表 t_er_contractsign

- **表名称：** 合同签订-主表
- **表名：** t_er_contractsign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcontractid | 合同id | int8 | 64 |  | √ | 0 | 合同id |
| 6 | fsigndate | 签约日期 | timestamp | 0 |  |  | null | 签约日期 |
| 7 | fsignaddressdetail | 详细签约地址 | varchar | 255 |  | √ | ' ' | 详细签约地址 |
| 8 | fpartbperson | 乙方签约人 | varchar | 80 |  | √ | ' ' | 乙方签约人 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fpartotherperson | 其他方签约人 | varchar | 80 |  | √ | ' ' | 其他方签约人 |
| 11 | fenddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsignaddress | 签约地址 | varchar | 50 |  | √ | ' ' | 签约地址 |
| 14 | fcontractbillno | 合同单据编号 | varchar | 80 |  | √ | ' ' | 合同单据编号 |
| 15 | fpartaperson | 甲方签约人 | varchar | 80 |  | √ | ' ' | 甲方签约人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_contractsign_fbno |  | fcontractbillno |
| 2 | pk_t_er_contractsign |  | fid |
