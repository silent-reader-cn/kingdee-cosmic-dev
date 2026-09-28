# 单据界面属性设置-wf_billpageattrcfgmodel

## 单据界面属性设置-主表 t_wf_billpageattrcfg

- **表名称：** 单据界面属性设置-主表
- **表名：** t_wf_billpageattrcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人id | int8 | 64 |  | √ | 0 | 修改人id |
| 3 | fname | 单据名称 | varchar | 500 |  | √ | ' ' | 单据名称 |
| 4 | fhide | 是否隐藏 | bpchar | 1 |  | √ | '0' | 是否隐藏 |
| 5 | fmodify | 是否可修改 | bpchar | 1 |  | √ | '0' | 是否可修改 |
| 6 | ffieldname | 字段名称 | varchar | 115 |  | √ | ' ' | 字段名称 |
| 7 | fpagenumber | 单据页面编码 | varchar | 50 |  | √ | ' ' | 单据页面编码 |
| 8 | fprocdefid | 流程定义id | int8 | 64 |  | √ | 0 | 流程定义id |
| 9 | fpagename | 单据页面名称 | varchar | 115 |  | √ | ' ' | 单据页面名称 |
| 10 | ffieldnumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fcreatorid | 创建人id | int8 | 64 |  | √ | 0 | 创建人id |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fnumber | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 15 | ftaskdefid | 节点id | varchar | 255 |  | √ | ' ' | 节点id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_billpageattrcfg_pdef |  | fprocdefid |
| 2 | t_wf_billpageattrcfg_pkey |  | fid |

---

## 单据界面属性设置-多语言表 t_wf_billpageattrcfg_l

- **表名称：** 单据界面属性设置-多语言表
- **表名：** t_wf_billpageattrcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 单据名称 | varchar | 500 |  | √ | ' ' | 单据名称 |
| 3 | ffieldname | 字段名称 | varchar | 115 |  | √ | ' ' | 字段名称 |
| 4 | fpagename | 单据页面名称 | varchar | 115 |  | √ | ' ' | 单据页面名称 |
| 5 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_billpageattrcfg_l_pkey |  | fpkid |
| 2 | idx_wf_billpageattrcfg_loc |  | fid,flocaleid |
