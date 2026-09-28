# 跨区域涉税事项报告-tcvat_cross_tax_report

## 合同信息-子表 t_tcvat_base_contract

- **表名称：** 合同信息-子表
- **表名：** t_tcvat_base_contract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fcontractno | 合同编码 | int8 | 64 |  | √ | 0 | 跨区域涉税报告合同信息 tcvat_base_contract_info |
| 5 | fcurrentamount | 本次报验合同金额 | numeric | 23 | 10 | √ | 0 | 本次报验合同金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_base_contract |  | fid |
| 2 | pk_tcvat_base_contract |  | fentryid |

---

## 跨区域涉税事项报告-主表 t_tcvat_cross_tax_report

- **表名称：** 跨区域涉税事项报告-主表
- **表名：** t_tcvat_cross_tax_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhandlerphone | 经办人手机 | varchar | 50 |  | √ | ' ' | 经办人手机 |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdatestart | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 6 | fhandlerlandline | 经办人座机 | varchar | 50 |  | √ | ' ' | 经办人座机 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbaseproject | 预缴项目编码 | int8 | 64 |  | √ | 0 | 预缴项目信息 tcvat_prepay_project_info |
| 9 | flinkphone | 联系人手机 | varchar | 50 |  | √ | ' ' | 联系人手机 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fnewdateend | 最新有效期止 | timestamp | 0 |  |  | null | 最新有效期止 |
| 12 | fcheckno | 报验管理编号 | varchar | 50 |  | √ | ' ' | 报验管理编号 |
| 13 | fislinkman | 经办人是否为跨区域涉税事项联系人 | bpchar | 1 |  | √ | '0' | 经办人是否为跨区域涉税事项联系人 |
| 14 | fmanagetype | 经营方式 | varchar | 50 |  | √ | ' ' | 经营方式,枚举: 建筑安装 :建筑安装 装饰修饰 :装饰修饰 修理修配 :修理修配 加工 :加工 批发 :批发 零售 :零售 批零兼营 :批零兼营 零批兼营 :零批兼营 其他 :其他 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fhandler | 经办人 | varchar | 50 |  | √ | ' ' | 经办人 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdateend | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 23 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | flinklandline | 联系人座机 | varchar | 50 |  | √ | ' ' | 联系人座机 |
| 26 | fcheckstatus | 报验状态 | varchar | 50 |  | √ | ' ' | 报验状态,枚举: nocheck :未报验 checked :已报验 feedback :已反馈 trash :已作废 delay :已延期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_cross_tax_report |  | fid |
| 2 | idx_tcvat_cross_tax_report |  | fbillno |
