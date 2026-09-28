# 决策方案-idi_schema

## 决策方案-主表 t_idi_decisionschema

- **表名称：** 决策方案-主表
- **表名：** t_idi_decisionschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fanalysismode | 分析方式 | varchar | 30 |  | √ | ' ' | 分析方式,枚举: score :评分 noscore :无评分 |
| 5 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | frule | 规则脚本 | varchar | 510 |  |  | null | 规则脚本 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | frule_tag | 规则脚本_详情 | text | 0 |  |  | null | 规则脚本_详情 |
| 12 | forder | 执行顺序 | int8 | 64 |  | √ | 1 | 执行顺序 |
| 13 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 15 | fdesc | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 16 | fsourceentitynumber | 源单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_decisionschema_ct |  | fcreatetime |
| 2 | idx_idi_decisionschema_enb |  | fenable |
| 3 | idx_idi_decisionschema_src |  | fsourceentitynumber |
| 4 | idx_idi_decisionschema_num |  | fnumber |
| 5 | t_idi_decisionschema_pkey |  | fid |

---

## 决策方案-多语言表 t_idi_decisionschema_l

- **表名称：** 决策方案-多语言表
- **表名：** t_idi_decisionschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_idi_decisionschema_l_pkey |  | fpkid |
| 2 | idx_idi_decisionschema_l_fid |  | fid |
