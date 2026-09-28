# 吸收成本调整单-sco_absorbadjust

## 单据体-子表 t_sco_absorbadjustentry

- **表名称：** 单据体-子表
- **表名：** t_sco_absorbadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_absorbadjustentry |  | fentryid |
| 2 | idx_sco_absorbadjustentry |  | fid,felementid,fsubelementid |

---

## 吸收成本调整单-主表 t_sco_absorbadjust

- **表名称：** 吸收成本调整单-主表
- **表名：** t_sco_absorbadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 6 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 7 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 10 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fsource | 数据来源 | bpchar | 1 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :计算 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdifftype | 差异类型 | bpchar | 1 |  | √ | ' ' | 差异类型,枚举: 2 :制造费用差异 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 17 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 18 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 19 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 20 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_absorbadjust |  | fid |
| 2 | idx_sco_absorbadjust |  | forgid,fcostaccountid,fperiodid |
