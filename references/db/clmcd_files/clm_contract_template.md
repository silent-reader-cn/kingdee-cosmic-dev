# 合同模板-clm_contract_template

## 合同模板-主表 t_clm_contract_template

- **表名称：** 合同模板-主表
- **表名：** t_clm_contract_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 合同类型分组 | int8 | 64 |  | √ | 0 | [合同类型分组 conm_typegroup](../conm_files/conm_typegroup.md) |
| 3 | ftemplatedatas | 模板变量 | text | 0 |  |  | null | 模板变量 |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | ftemplatetype | 模板类型 | varchar | 50 |  | √ | ' ' | 模板类型,枚举: STACON :标准合同 FRAAGR :框架协议 SUPAGR :补充协议 TERAGR :终止协议 |
| 7 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fconmtype | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 14 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | ftemplatedatas_tag | 模板变量_详情 | text | 0 |  |  | null | 模板变量_详情 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | ffileid | 文件id | int8 | 64 |  | √ | 0 | 文件id |
| 22 | fcontractpartytype | fcontractpartytype | varchar | 50 |  | √ | ' ' |  |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fisallowsubmit | 是否允许提交 | bpchar | 1 |  | √ | '0' | 是否允许提交 |
| 25 | fisallowededit | 使用模板起草时，可编辑模板文本 | bpchar | 1 |  | √ | '0' | 使用模板起草时，可编辑模板文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_contract_template |  | fid |
| 2 | idx_clm_con_template_number |  | fnumber |

---

## 合同模板-多语言表 t_clm_contract_template_l

- **表名称：** 合同模板-多语言表
- **表名：** t_clm_contract_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 3 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_contract_template_l_fid |  | fid,flocaleid |
| 2 | pk_t_clm_contract_template_l |  | fpkid |
