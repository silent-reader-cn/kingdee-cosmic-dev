# 单据摘要信息-wf_mbillsummary_cfg

## 单据摘要信息-多语言表 t_wf_mbillsummarycfg_l

- **表名称：** 单据摘要信息-多语言表
- **表名：** t_wf_mbillsummarycfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_mbillsummarycfg_l_pkey |  | fpkid |
| 2 | idx_wf_mbillsummarycfg_l |  | fid,flocaleid |

---

## 单据体-多语言表 t_wf_mbillsumarycfgentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_wf_mbillsumarycfgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | 字段名称 | varchar | 230 |  | √ | ' ' | 字段名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fshowcontentmul | 显示内容 | varchar | 2000 |  | √ | ' ' | 显示内容 |
| 6 | fentrylocationname | 分录名称 | varchar | 230 |  | √ | ' ' | 分录名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_mbillsumcfgentry_l |  | fentryid,flocaleid |
| 2 | t_wf_mbillsumarycfgentry_l_pkey |  | fpkid |

---

## 单据体-子表 t_wf_mbillsumarycfgentry

- **表名称：** 单据体-子表
- **表名：** t_wf_mbillsumarycfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrylocation | 分录标识 | varchar | 36 |  | √ | ' ' | 分录标识 |
| 3 | fisdefaultshow | 单据头与分录打平时显示分录 | bpchar | 1 |  | √ | '1' | 单据头与分录打平时显示分录 |
| 4 | ffieldname | ffieldname | varchar | 230 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentrylocationid | 分录id | varchar | 36 |  | √ | ' ' | 分录id |
| 7 | ffontsize | 字体大小(px) | int8 | 64 |  | √ | 0 | 字体大小(px) |
| 8 | frefparentpropfieldid | 关联的父属性id | varchar | 50 |  | √ | ' ' | 关联的父属性id |
| 9 | fisheadfield | 单据头字段 | bpchar | 1 |  | √ | '0' | 单据头字段 |
| 10 | ffieldid | 字段id | varchar | 36 |  | √ | ' ' | 字段id |
| 11 | feditable | 是否可编辑 | bpchar | 1 |  | √ | '0' | 是否可编辑 |
| 12 | fshowcontentmul | 显示内容 | varchar | 2000 |  | √ | ' ' | 显示内容 |
| 13 | fentrylocationname | fentrylocationname | varchar | 230 |  | √ | ' ' |  |
| 14 | ffieldkey | 字段标识 | varchar | 36 |  | √ | ' ' | 字段标识 |
| 15 | faggregatefunction | 聚合函数 | varchar | 30 |  | √ | ' ' | 聚合函数,枚举: sum :SUM count :COUNT |
| 16 | ffieldpercen | 字段占比(%,px) | varchar | 10 |  | √ | ' ' | 字段占比(%,px) |
| 17 | ffieldtype | 字段类型 | varchar | 36 |  | √ | ' ' | 字段类型 |
| 18 | fcontent | fcontent | varchar | 2000 |  | √ | ' ' |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | ffontcolor | 字体颜色(#FFFFFF) | varchar | 36 |  | √ | ' ' | 字体颜色(#FFFFFF) |
| 21 | fshowcontent | 显示内容 | varchar | 2000 |  | √ | ' ' | 显示内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_mbillsumarycfgentry_pkey |  | fentryid |
| 2 | idx_wf_mbillsumcfgentry_fid |  | fid |

---

## 单据摘要信息-主表 t_wf_mbillsummarycfg

- **表名称：** 单据摘要信息-主表
- **表名：** t_wf_mbillsummarycfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsummarytpl | 单据模板编码 | varchar | 100 |  | √ | ' ' | 单据模板编码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | fname | varchar | 230 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fdefaultdatarows | 分录数据默认显示行数 | int8 | 64 |  | √ | 0 | 分录数据默认显示行数 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fscene | 使用场景 | varchar | 50 |  | √ | ' ' | 使用场景,枚举: mobileSummary :移动单据摘要 flowchartSummary :业务流程图侧边栏单据摘要 floatlayerSummary :业务流程图浮动层单据摘要 billRelationCardSummary :单据关系图卡片摘要 billRelationStackedCardSummary :单据关系图堆叠卡片摘要 |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 13 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 14 | ftplname | 摘要模板 | varchar | 100 |  | √ | ' ' | 摘要模板 |
| 15 | fbilltype | 单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 16 | fdefaultrows | 默认显示行数 | int8 | 64 |  | √ | 0 | 默认显示行数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_mbillsummarycfg_num |  | fnumber |
| 2 | t_wf_mbillsummarycfg_pkey |  | fid |
