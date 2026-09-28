# 质量云插件映射-qcbd_plugin_cfg

## 质量云插件映射-多语言表 t_qcbd_plugin_cfg_l

- **表名称：** 质量云插件映射-多语言表
- **表名：** t_qcbd_plugin_cfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_plugin_cfg_l |  | fpkid |
| 2 | idx_qcbd_pluginl_fname |  | fname |
| 3 | idx_qcbd_pluginl_fid |  | fid,flocaleid |

---

## 质量云插件映射-主表 t_qcbd_plugin_cfg

- **表名称：** 质量云插件映射-主表
- **表名：** t_qcbd_plugin_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | froute | 插件路径 | varchar | 255 |  | √ | ' ' | 插件路径 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fentitytypeid | 实体类型 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fplugintype | 插件类型 | varchar | 5 |  | √ | ' ' | 插件类型,枚举: A :检验对象操作插件 |
| 10 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_plugin_cfg |  | fid |
| 2 | idx_qcbd_plugin_fcreatetime |  | fcreatetime |
| 3 | idx_qcbd_plugin_fnumber |  | fnumber |

---

## 检验结果插件单据体-子表 t_qcbd_pg_resentry

- **表名称：** 检验结果插件单据体-子表
- **表名：** t_qcbd_pg_resentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresplugindesc | 插件说明 | varchar | 512 |  | √ | ' ' | 插件说明 |
| 3 | fresopreate | 操作 | varchar | 10 |  | √ | ' ' | 操作,枚举: audit :审核 unaudit :反审核 submit :提交 unsubmit :反提交 save :保存 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fresenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 6 | fresplugin | 插件 | varchar | 512 |  | √ | ' ' | 插件 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_pg_fseq |  | fseq |
| 2 | pk_qcbd_pg_resentry |  | fentryid |
| 3 | idx_qcbd_pg_fid |  | fid |
