# 移动销售显示设置-mscm_smbillcfg

## 单据头字段信息-多语言表 t_mscm_smbillcfghentity_l

- **表名称：** 单据头字段信息-多语言表
- **表名：** t_mscm_smbillcfghentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | ffieldname | varchar | 255 |  | √ | ' ' |  |
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
| 1 | idx_mscm_smbillcfghentity_l_il |  | fentryid,flocaleid |
| 2 | pk_mscm_smbillcfghentity_l |  | fpkid |

---

## 移动销售显示设置-多语言表 t_mscm_smbillcfg_l

- **表名称：** 移动销售显示设置-多语言表
- **表名：** t_mscm_smbillcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 单据名称（模版） | varchar | 255 |  | √ | ' ' | 单据名称（模版） |
| 3 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscm_smbillcfg_l_idloc |  | fid,flocaleid |
| 2 | pk_mscm_smbillcfg_l |  | fpkid |

---

## 移动销售显示设置-主表 t_mscm_smbillcfg

- **表名称：** 移动销售显示设置-主表
- **表名：** t_mscm_smbillcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 4 | fshowstyle | fshowstyle | varchar | 5 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbillname | 单据名称 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fpreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 15 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscm_smbillcfg_bn_e |  | fenable,fbillname |
| 2 | pk_mscm_smbillcfg |  | fid |
| 3 | idx_mscm_smbillcfg_num_pre |  | fpreset,fbillname |

---

## 单据头字段信息-子表 t_mscm_smbillcfghentity

- **表名称：** 单据头字段信息-子表
- **表名：** t_mscm_smbillcfghentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feditshow | 编辑时显示 | bpchar | 1 |  | √ | ' ' | 编辑时显示 |
| 3 | frequiredfield | 必选字段 | bpchar | 1 |  | √ | ' ' | 必选字段 |
| 4 | ffieldname | ffieldname | varchar | 255 |  | √ | ' ' |  |
| 5 | fbelongcard | 所属卡片 | varchar | 100 |  | √ | ' ' | 所属卡片,枚举: |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | flitemodeshow | 精简模式显示 | bpchar | 1 |  | √ | ' ' | 精简模式显示 |
| 8 | ffieldid | 字段内码 | varchar | 36 |  | √ | ' ' | 字段内码 |
| 9 | ffieldkey | 字段标识 | varchar | 36 |  | √ | ' ' | 字段标识 |
| 10 | frequired | 必录 | bpchar | 1 |  | √ | ' ' | 必录 |
| 11 | fviewshow | 查看时显示 | bpchar | 1 |  | √ | ' ' | 查看时显示 |
| 12 | ffieldtype | 字段类型 | varchar | 80 |  | √ | ' ' | 字段类型 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mscm_smbillcfghentity |  | fentryid |
| 2 | idx_mscm_smbillcfghentity_fid |  | fid |

---

## 单据体字段信息-多语言表 t_mscm_smbillcfgeentity_l

- **表名称：** 单据体字段信息-多语言表
- **表名：** t_mscm_smbillcfgeentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | ffieldname | varchar | 255 |  | √ | ' ' |  |
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
| 1 | pk_mscm_smbillcfgeentity_l |  | fpkid |
| 2 | idx_mscm_smbillcfgeentity_l_il |  | fentryid,flocaleid |

---

## 单据体字段信息-子表 t_mscm_smbillcfgeentity

- **表名称：** 单据体字段信息-子表
- **表名：** t_mscm_smbillcfgeentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feditshow | 编辑时显示 | bpchar | 1 |  | √ | ' ' | 编辑时显示 |
| 3 | frequiredfield | 必选字段 | bpchar | 1 |  | √ | ' ' | 必选字段 |
| 4 | ffieldname | ffieldname | varchar | 255 |  | √ | ' ' |  |
| 5 | fbelongcard | 所属卡片 | varchar | 100 |  | √ | ' ' | 所属卡片,枚举: |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | flitemodeshow | 精简模式显示 | bpchar | 1 |  | √ | ' ' | 精简模式显示 |
| 8 | ffieldid | 字段内码 | varchar | 36 |  | √ | ' ' | 字段内码 |
| 9 | ffieldkey | 字段标识 | varchar | 36 |  | √ | ' ' | 字段标识 |
| 10 | frequired | 必录 | bpchar | 1 |  | √ | ' ' | 必录 |
| 11 | fviewshow | 查看时显示 | bpchar | 1 |  | √ | ' ' | 查看时显示 |
| 12 | ffieldtype | 字段类型 | varchar | 80 |  | √ | ' ' | 字段类型 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mscm_smbillcfgeentity |  | fentryid |
| 2 | idx_mscm_smbillcfgeentity_fid |  | fid |
