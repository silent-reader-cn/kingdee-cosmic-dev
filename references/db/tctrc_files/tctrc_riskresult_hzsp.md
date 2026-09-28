# 风险处理汇总审批单-tctrc_riskresult_hzsp

## 风险处理汇总审批单-主表 t_tctrc_riskresult_hzsp

- **表名称：** 风险处理汇总审批单-主表
- **表名：** t_tctrc_riskresult_hzsp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fhzamount | 汇总金额 | numeric | 23 | 4 | √ | 0 | 汇总金额 |
| 5 | fhzsprule | 汇总审批规则名称 | int8 | 64 |  | √ | 0 | [汇总审批规则 tctb_hzsp_rule](../tctb_files/tctb_hzsp_rule.md) |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fhzspruletype | 汇总审批规则类型 | int8 | 64 |  | √ | 0 | [汇总审批规则类型 tctb_hzsp_rule_type](../tctb_files/tctb_hzsp_rule_type.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fhzspbilltype | 汇总审批单据类型 | int8 | 64 |  | √ | 0 | [汇总审批单据类型 tctb_hzsp_bill_type](../tctb_files/tctb_hzsp_bill_type.md) |
| 16 | fbillno | 汇总审批单编号 | varchar | 30 |  | √ | ' ' | 汇总审批单编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_riskresult_hzsp |  | fid |

---

## 主表-子表 t_tctrc_riskresult_detail

- **表名称：** 主表-子表
- **表名：** t_tctrc_riskresult_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdealresult | 处理结果 | varchar | 50 |  | √ | ' ' | 处理结果,枚举: 1 :- 2 :正常 3 :风险 |
| 3 | frisk | 风险 | int8 | 64 |  | √ | 0 | [风险设置 tctrc_risk_definition](../tctrc_files/tctrc_risk_definition.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fresult | 风险结果 | varchar | 50 |  | √ | ' ' | 风险结果 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :正常 B :已变更 C :已删除 |
| 8 | fenddate | 计算时间止 | timestamp | 0 |  |  | null | 计算时间止 |
| 9 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstartdate | 计算时间起 | timestamp | 0 |  |  | null | 计算时间起 |
| 11 | frunorg | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fbillid | 单据ID | varchar | 100 |  | √ | ' ' | 单据ID |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | frlevel | 风险等级基础资料 | int8 | 64 |  | √ | 0 | [风险等级 tctrc_risk_level](../tctrc_files/tctrc_risk_level.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_riskresult_detail |  | fentryid |
| 2 | idx_tctrc_riskresult_detail |  | fid |

---

## 附件-附件表 t_tctrc_riskresult_attach

- **表名称：** 附件-附件表
- **表名：** t_tctrc_riskresult_attach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_riskresult_attach |  | fpkid |
| 2 | idx_tctrc_riskresult_attach |  | fdetailid |

---

## 子表-子表 t_tctrc_riskresult_item

- **表名称：** 子表-子表
- **表名：** t_tctrc_riskresult_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fhandleoption | 处理意见 | varchar | 2000 |  | √ | ' ' | 处理意见 |
| 2 | fhandler | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fresult | 处理结果 | varchar | 50 |  | √ | ' ' | 处理结果,枚举: 1 :- 2 :正常 3 :风险 4 :重新计算 5 :取消处理 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fsubbillid | 单据子表ID | varchar | 100 |  | √ | ' ' | 单据子表ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_riskresult_item |  | fdetailid |
| 2 | idx_tctrc_riskresult_item |  | fentryid |
