# 报表项目-xkbd_rptitem

## 预警设置分录-子表 t_xkbd_rptitemwarning

- **表名称：** 预警设置分录-子表
- **表名：** t_xkbd_rptitemwarning

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fwarningcolor | 预警颜色 | varchar | 50 |  | √ | ' ' | 预警颜色,枚举: red :红 orange :橙 yellow :黄 |
| 2 | fwarningitemenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 3 | fwarninglimitdesc | 预警条件 | varchar | 2000 |  | √ | ' ' | 预警条件 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fwarningtip | 预警提示语 | varchar | 255 |  | √ | ' ' | 预警提示语 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 8 | fitemid | fitemid | int8 | 64 |  | √ | 0 |  |
| 9 | fwarninglimit | 预警值条件表达式 | varchar | 2000 |  | √ | ' ' | 预警值条件表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbd_rptitemwarning |  | fentryid |
| 2 | idx_xkbd_rptitemwarn_fitemid |  | fitemid |

---

## 报表项目-多语言表 t_xkbd_rptitem_l

- **表名称：** 报表项目-多语言表
- **表名：** t_xkbd_rptitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | frptshowname | 报表显示名称 | varchar | 255 |  | √ | ' ' | 报表显示名称 |
| 3 | fcustomproperty | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 4 | fmulnotes | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | facctformulatxt | facctformulatxt | varchar | 255 |  | √ | ' ' |  |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fitemid | fitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbd_rptitem_l_fitemid |  | fitemid |
| 2 | pk_xkbd_rptitem_l |  | fpkid |

---

## 预警设置分录-多语言表 t_xkbd_rptitemwarning_l

- **表名称：** 预警设置分录-多语言表
- **表名：** t_xkbd_rptitemwarning_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fwarningtip | 预警提示语 | varchar | 255 |  | √ | ' ' | 预警提示语 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbd_rptitemwarning_l |  | fpkid |
| 2 | idx_xkbd_rptitemwarn_l_entryid |  | fentryid,flocaleid |

---

## 报表项目-主表 t_xkbd_rptitem

- **表名称：** 报表项目-主表
- **表名：** t_xkbd_rptitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 报表项目分组 xkbd_rptitemgroup |
| 2 | fproportionbase | 占比基数 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 3 | fitemdc | 方向 | varchar | 30 |  | √ | ' ' | 方向,枚举: 1 :借 -1 :贷 |
| 4 | frptshowname | 报表显示名称 | varchar | 255 |  | √ | ' ' | 报表显示名称 |
| 5 | fmulnotes | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fnotes | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fisparent | 是否为父级 | bpchar | 1 |  | √ | ' ' | 是否为父级 |
| 8 | fistext | 文本项 | bpchar | 1 |  | √ | '0' | 文本项 |
| 9 | fissumitem | 合计项 | bpchar | 1 |  | √ | '0' | 合计项 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftextfield | 原上级项目内码(虚拟字段) | varchar | 255 |  | √ | ' ' | 原上级项目内码(虚拟字段) |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | faccttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 16 | fisproportionanalysis | 特殊占比分析 | bpchar | 1 |  | √ | ' ' | 特殊占比分析 |
| 17 | flevelcode | 层级码 | varchar | 30 |  | √ | ' ' | 层级码 |
| 18 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 19 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fparentid | 父级项目 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fcustomproperty | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 26 | frptitemid | 项目 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 27 | fcashitemtbid | 现金流量项目表 | int8 | 64 |  | √ | 0 | 现金流量项目表 gl_cashflowitemtb |
| 28 | fitemid | fitemid | int8 | 64 |  | √ | 0 | id |
| 29 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 1 :逐级分配 2 :自由分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 30 | fcustomptynew | 类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 31 | fcashflowid | 现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 32 | fiswarninganalysis | 预警分析 | bpchar | 1 |  | √ | ' ' | 预警分析 |
| 33 | facctid | 科目 | varchar | 30 |  | √ | ' ' | 科目 |
| 34 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | facctformula | 关系表达式 | varchar | 2000 |  | √ | ' ' | 关系表达式 |
| 36 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 37 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | facctformulatxt | facctformulatxt | varchar | 255 |  | √ | ' ' |  |
| 39 | fdataresource | 取数来源 | varchar | 30 |  | √ | ' ' | 取数来源,枚举: 1 :科目 2 :现金流量项目 3 :报表项目 |
| 40 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 41 | fcombofield | 数据来源(虚字段) | varchar | 255 |  | √ | ' ' | 数据来源(虚字段),枚举: 0 :手工新增 1 :科目引入 2 :现金流量引入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fitemid | fitemid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbd_rptitem_fnumber |  | fnumber |
| 2 | pk_xkbd_rptitem |  | fitemid |
