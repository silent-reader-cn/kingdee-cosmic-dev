# 单据自定义属性设置-mpm_billcustomfieldset

## 单据体-子表 t_mpm_billfieldsetentry

- **表名称：** 单据体-子表
- **表名：** t_mpm_billfieldsetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprecision | 总体精度 | int4 | 32 |  | √ | 0 | 总体精度 |
| 3 | ffielddisplayname | 字段显示名 | varchar | 80 |  | √ | ' ' | 字段显示名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fismust | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 6 | fentrybillobjectid | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | ffieldtype | 字段类型 | bpchar | 1 |  | √ | ' ' | 字段类型,枚举: A :文本 B :数字 C :日期 D :复选框 |
| 8 | fsrclibfield | 关联属性库字段 | int8 | 64 |  | √ | 0 | 自定义属性库 mpm_customproplib |
| 9 | fscale | 小数精度 | int4 | 32 |  | √ | 0 | 小数精度 |
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

## 单据体-多语言表 t_mpm_billfieldsetentry_l

- **表名称：** 单据体-多语言表
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

---

## 单据自定义属性设置-多语言表 t_mpm_billcustomfieldset_l

- **表名称：** 单据自定义属性设置-多语言表
- **表名：** t_mpm_billcustomfieldset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_billcustomfieldset_l |  | fpkid |
| 2 | idx_mpm_billcustfldset_l |  | fid,flocaleid |

---

## 单据自定义属性设置-主表 t_mpm_billcustomfieldset

- **表名称：** 单据自定义属性设置-主表
- **表名：** t_mpm_billcustomfieldset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fpublishstatus | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: A :未发布 B :已发布 |
| 5 | fbillobjectid | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | flastpublisher | 最近发布人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | flastpublishtime | 最近发布时间 | timestamp | 0 |  |  | null | 最近发布时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_billcustfldset_no |  | fnumber |
| 2 | pk_mpm_billcustomfieldset |  | fid |
| 3 | idx_mpm_billcustfldset_bo |  | fbillobjectid |
