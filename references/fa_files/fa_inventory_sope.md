# 盘点范围(原我的盘点任务)-fa_inventory_sope

## 盘点范围(原我的盘点任务)-多语言表 t_fa_inventschemeentry_l

- **表名称：** 盘点范围(原我的盘点任务)-多语言表
- **表名：** t_fa_inventschemeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | fremark | varchar | 200 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_inventschemeentry_l_pkey |  | fpkid |
| 2 | idx_fa_inventschemeentry_l |  | fentryid,flocaleid |

---

## 盘点范围(原我的盘点任务)-主表 t_fa_inventschemeentry

- **表名称：** 盘点范围(原我的盘点任务)-主表
- **表名：** t_fa_inventschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 盘点方案id | int8 | 64 |  | √ | 0 | 盘点方案 fa_inventscheme_new |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fqtytypevalue | fqtytypevalue | varchar | 10 |  | √ | '0' |  |
| 5 | fchargepersonid | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffiltercondition_tag | ffiltercondition_tag | text | 0 |  |  | ' ' |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 生成状态 | bpchar | 1 |  | √ | 'A' | 生成状态,枚举: A :未下达 B :已下达 C :已生成 |
| 11 | finventschemeentryid | finventschemeentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fassetunitid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | ffinaccountdate | 入账截止日期 | timestamp | 0 |  |  | null | 入账截止日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | ftaskrule | 任务拆分规则 | varchar | 50 |  | √ | ' ' | 任务拆分规则 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | ffiltercondition | ffiltercondition | varchar | 512 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_inventschemeentry_fid |  | fid |
| 2 | t_fa_inventschemeentry_pkey |  | fentryid |
