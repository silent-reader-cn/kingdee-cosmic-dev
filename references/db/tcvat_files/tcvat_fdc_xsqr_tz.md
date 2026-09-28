# 房地产销售确认台账-tcvat_fdc_xsqr_tz

## 台账详情-子表 t_tcvat_fdc_xsqrtz_entry

- **表名称：** 台账详情-子表
- **表名：** t_tcvat_fdc_xsqrtz_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdqkpxse | （8）当期开票销售额 | numeric | 23 | 10 | √ | 0 | （8）当期开票销售额 |
| 3 | fdqwkpxse | （9）当期未开票销售额（10-8） | numeric | 23 | 10 | √ | 0 | （9）当期未开票销售额（10-8） |
| 4 | fdsjrksmj | （12）地上计容可售面积 | numeric | 23 | 10 | √ | 0 | （12）地上计容可售面积 |
| 5 | froomid | 房间名称 | int8 | 64 |  | √ | 0 | [房间基础信息 bastax_room](../bastax_files/bastax_room.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fwqkpxse | （5）往期开票销售额（上期3） | numeric | 23 | 10 | √ | 0 | （5）往期开票销售额（上期3） |
| 8 | fdqskjebhs | （7）当期收款金额（不含税） | numeric | 23 | 10 | √ | 0 | （7）当期收款金额（不含税） |
| 9 | fljskjebhs | （2）累计收款金额（不含税） | numeric | 23 | 10 | √ | 0 | （2）累计收款金额（不含税） |
| 10 | fljkpxse | （3）累计开票销售额（5+8） | numeric | 23 | 10 | √ | 0 | （3）累计开票销售额（5+8） |
| 11 | fljwkpxse | （4）累计未开票销售额（6+9） | numeric | 23 | 10 | √ | 0 | （4）累计未开票销售额（6+9） |
| 12 | fqyjebhs | （1）签约金额(不含税) | numeric | 23 | 10 | √ | 0 | （1）签约金额(不含税) |
| 13 | fwqwkpxse | （6）往期未开票销售额（上期4） | numeric | 23 | 10 | √ | 0 | （6）往期未开票销售额（上期4） |
| 14 | fdqqrxsebl | （11）当期确认销售额占签约金额比例（10/1） | numeric | 23 | 10 | √ | 0 | （11）当期确认销售额占签约金额比例（10/1） |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fdqqrxse | （10）当期确认销售额 | numeric | 23 | 10 | √ | 0 | （10）当期确认销售额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fdc_xsqrtz_entry_fk |  | fid |
| 2 | pk_tcvat_fdc_xsqrtz_entry |  | fentryid |

---

## 房地产销售确认台账-主表 t_tcvat_fdc_xsqrtz

- **表名称：** 房地产销售确认台账-主表
- **表名：** t_tcvat_fdc_xsqrtz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstage | 工程项目分期 | int8 | 64 |  | √ | 0 | [分期信息 bastax_stage](../bastax_files/bastax_stage.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fdqqrxsehj | 当期确认销售额 | numeric | 23 | 10 | √ | 0 | 当期确认销售额 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 13 | fdqkpxsehj | 当期开票销售额 | numeric | 23 | 10 | √ | 0 | 当期开票销售额 |
| 14 | fdqwkpxsehj | 当期未开票销售额 | numeric | 23 | 10 | √ | 0 | 当期未开票销售额 |
| 15 | fproject | 税务项目 | int8 | 64 |  | √ | 0 | [税务项目信息 bastax_taxproject](../bastax_files/bastax_taxproject.md) |
| 16 | fbillno | 台账编号 | varchar | 30 |  | √ | ' ' | 台账编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_fdc_xsqrtz |  | fid |
| 2 | idx_t_tcvat_fdc_xsqrtz_uniq1 |  | forgid,fproject,fstage,fskssqq,fskssqz |
