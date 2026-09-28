# 字段权限方案-perm_fieldscheme

## 字段权限方案-主表 t_perm_fieldscheme

- **表名称：** 字段权限方案-主表
- **表名：** t_perm_fieldscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcontrolfieldtype | 控件字段类型 | varchar | 255 |  | √ | ' ' | 控件字段类型,枚举: |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffieldfrom | 字段来源类型 | varchar | 10 |  | √ | '2' | 字段来源类型,枚举: 2 :按字段 1 :按字段属性 |
| 7 | fcontrolmode | 控制模式 | varchar | 10 |  | √ | ' ' | 控制模式,枚举: 10 :禁止查看 20 :禁止编辑 |
| 8 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsensitive | 敏感字段方案 | bpchar | 1 |  | √ | '0' | 敏感字段方案 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fissystem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 15 | fentnum | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 18 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_fieldscheme |  | fid |
| 2 | idx_perm_fieldscheme_num |  | fnumber |

---

## 字段权限方案-多语言表 t_perm_fieldscheme_l

- **表名称：** 字段权限方案-多语言表
- **表名：** t_perm_fieldscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_fieldscheme_l |  | fpkid |
| 2 | idx_perm_fieldscheme_l |  | fid,flocaleid |

---

## 字段明细-子表 t_perm_fieldschemed

- **表名称：** 字段明细-子表
- **表名：** t_perm_fieldschemed

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段编码 | varchar | 255 |  | √ | ' ' | 字段编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcontrolmode | 权限 | varchar | 10 |  | √ | ' ' | 权限 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_fieldschemed |  | fentryid |
| 2 | idx_fpsd_fielname |  | ffieldname |
