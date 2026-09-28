# 合同评审规则设置-clm_contract_review_rule

## 指定人员-多选基础资料表 t_clm_review_srdesignee

- **表名称：** 指定人员-多选基础资料表
- **表名：** t_clm_review_srdesignee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_clm_review_srdesignee_fk |  | fid |
| 2 | pk_t_clm_review_srdesignee |  | fpkid |

---

## 适用合同类型-多选基础资料表 t_clm_review_conm_type

- **表名称：** 适用合同类型-多选基础资料表
- **表名：** t_clm_review_conm_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_review_conm_type_id |  | fid |
| 2 | pk_t_clm_review_conm_type |  | fpkid |

---

## 指定人员-多选基础资料表 t_clm_review_sadesignee

- **表名称：** 指定人员-多选基础资料表
- **表名：** t_clm_review_sadesignee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_review_sadesignee |  | fpkid |
| 2 | idx_clm_review_sadesignee_fk |  | fid |

---

## 合同评审规则设置-主表 t_clm_con_review_rule

- **表名称：** 合同评审规则设置-主表
- **表名：** t_clm_con_review_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 4 | fallowothersinvite | 允许评审参与人员在评审过程中邀请其他人员加入评审 | bpchar | 1 |  |  | '0' | 允许评审参与人员在评审过程中邀请其他人员加入评审 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | famendmenttypectrl | famendmenttypectrl | varchar | 50 |  | √ | ' ' |  |
| 7 | fendroundcondition | 【结束本轮评审】条件 | varchar | 50 |  | √ | ' ' | 【结束本轮评审】条件,枚举: NONE :不控制 ALL_REVIEW_PASS :评审人员全部评审通过 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsubmitapprovectrl | 【提交审批】操作权限 | varchar | 50 |  | √ | ' ' | 【提交审批】操作权限,枚举: NONE :不控制 ONLY_PROMOTER :仅限评审发起人 ASSIGNER :指定人员 |
| 11 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstartnewroundctrl | 【发起新一轮评审】操作权限 | varchar | 50 |  | √ | ' ' | 【发起新一轮评审】操作权限,枚举: NONE :不控制 ONLY_PROMOTER :仅限评审发起人 ASSIGNER :指定人员 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fendroundtextctrl | 【结束本轮评审】后的文本控制 | varchar | 50 |  | √ | ' ' | 【结束本轮评审】后的文本控制,枚举: PROHIBIT_EDITING :禁止内容编辑 ONLY_PROMOTER_EDIT :评审发起人可继续编辑文本 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fcondrafttype | 合同起草方式 | varchar | 50 |  | √ | ' ' | 合同起草方式,枚举: FORM_TPL :使用模板起草 UPLOAD_FILE :上传文件起草 |
| 23 | fendround | 【结束本轮评审】操作权限 | varchar | 50 |  | √ | ' ' | 【结束本轮评审】操作权限,枚举: NONE :不控制 ONLY_PROMOTER :仅限评审发起人 ASSIGNER :指定人员 |
| 24 | fcontracttype | fcontracttype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_con_review_rule_contype |  | fcontracttype |
| 2 | pk_t_clm_con_review_rule |  | fid |

---

## 指定人员-多选基础资料表 t_clm_review_erdesignee

- **表名称：** 指定人员-多选基础资料表
- **表名：** t_clm_review_erdesignee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_review_erdesignee |  | fpkid |
| 2 | idx_clm_review_erdesignee_fk |  | fid |

---

## 合同评审规则设置-多语言表 t_clm_con_review_rule_l

- **表名称：** 合同评审规则设置-多语言表
- **表名：** t_clm_con_review_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_con_review_rule_l_fid |  | fid,flocaleid |
| 2 | pk_t_clm_con_review_rule_l |  | fpkid |
