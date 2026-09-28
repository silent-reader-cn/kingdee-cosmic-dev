# 成本报表-tdm_costrpt

## 成本报表-主表 t_tdm_costrpt

- **表名称：** 成本报表-主表
- **表名：** t_tdm_costrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 编制组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fversionid | 版本 | int8 | 64 |  | √ | 0 | 标签设置 tctb_label_group |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcostreporttplid | 报表模板 | int8 | 64 |  | √ | 0 | 成本报表模板 tdm_costtpl |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fcostperiod | 成本分期 | varchar | 50 |  | √ | ' ' | 成本分期,枚举: 1 :一期 2 :二期 3 :三期 4 :四期 5 :五期 6 :六期 7 :七期 8 :八期 9 :九期 10 :十期 |
| 15 | ftaxprojectid | 税务项目 | int8 | 64 |  | √ | 0 | 税务项目信息 bastax_taxproject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_costrpt |  | fid |
| 2 | idx_tdm_costrpt_1 |  | fcreateorgid,ftaxprojectid,fversionid |

---

## 单据体-子表 t_tdm_costrpt_entry

- **表名称：** 单据体-子表
- **表名：** t_tdm_costrpt_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 3 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 4 | fisleaf | 是否叶子节点 | bpchar | 1 |  | √ | '0' | 是否叶子节点 |
| 5 | fparentid | 上级成本项目 | int8 | 64 |  | √ | 0 | 成本项目 tdm_costitem |
| 6 | ftax | 增值税税额 | numeric | 23 | 10 | √ | 0 | 增值税税额 |
| 7 | fperiodnum | 分期 | int8 | 64 |  | √ | 0 | 分期 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fcostitemid | 成本项目编码 | int8 | 64 |  | √ | 0 | 成本项目 tdm_costitem |
| 10 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_costrpt_entry_fk |  | fid |
| 2 | pk_tdm_costrpt_entry |  | fentryid |

---

## 成本报表-多语言表 t_tdm_costrpt_l

- **表名称：** 成本报表-多语言表
- **表名：** t_tdm_costrpt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_costrpt_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_costrpt_l |  | fpkid |
