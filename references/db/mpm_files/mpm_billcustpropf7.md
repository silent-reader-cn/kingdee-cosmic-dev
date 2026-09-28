# 单据自定义属性F7-mpm_billcustpropf7

## 单据自定义属性F7-主表 t_mpm_billfieldsetentry

- **表名称：** 单据自定义属性F7-主表
- **表名：** t_mpm_billfieldsetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprecision | fprecision | int4 | 32 |  | √ | 0 |  |
| 3 | ffielddisplayname | 字段显示名 | varchar | 80 |  | √ | ' ' | 字段显示名 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fismust | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 6 | fentrybillobjectid | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | ffieldtype | 字段类型 | bpchar | 1 |  | √ | ' ' | 字段类型,枚举: A :文本 B :数字 C :日期 D :复选框 |
| 8 | fsrclibfield | fsrclibfield | int8 | 64 |  | √ | 0 |  |
| 9 | fscale | fscale | int4 | 32 |  | √ | 0 |  |
| 10 | ffieldidenti | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 11 | fenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fentrypublishstatus | 字段发布状态 | bpchar | 1 |  | √ | ' ' | 字段发布状态,枚举: A :未发布 B :已发布 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_billfldsetentry_id |  | fid |
| 2 | pk_mpm_billfieldsetentry |  | fentryid |

---

## 单据自定义属性F7-多语言表 t_mpm_billfieldsetentry_l

- **表名称：** 单据自定义属性F7-多语言表
- **表名：** t_mpm_billfieldsetentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffielddisplayname | 字段显示名 | varchar | 255 |  | √ | ' ' | 字段显示名 |
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
| 1 | pk_mpm_billfieldsetentry_l |  | fpkid |
| 2 | idx_mpm_billfldsetentry_l |  | fentryid,flocaleid |
