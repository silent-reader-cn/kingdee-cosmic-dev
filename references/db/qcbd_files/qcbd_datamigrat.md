# 数据迁移工具_质量云-qcbd_datamigrat

## 单据体-子表 t_qcbd_migratentry

- **表名称：** 单据体-子表
- **表名：** t_qcbd_migratentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrctable | 源表名 | varchar | 50 |  | √ | ' ' | 源表名 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsrcfield | fsrcfield | varchar | 50 |  | √ | ' ' |  |
| 5 | fsrcfieldtag | 字段标志 | varchar | 50 |  | √ | ' ' | 字段标志 |
| 6 | fsrcfieldtagname | 字段标志名称 | varchar | 50 |  | √ | ' ' | 字段标志名称 |
| 7 | fismutilan | 多语言字段 | bpchar | 1 |  | √ | '0' | 多语言字段 |
| 8 | freflexcfg | 表映射配置 | int8 | 64 |  | √ | 0 | [表映射配置_质量云 qcbd_tablereflexcfg](../qcbd_files/qcbd_tablereflexcfg.md) |
| 9 | fdesfield | 目标字段名 | varchar | 50 |  | √ | ' ' | 目标字段名 |
| 10 | fparentdestable | 上级目标表名 | varchar | 50 |  | √ | '' | 上级目标表名 |
| 11 | fexpfix | 扩展表后缀 | varchar | 50 |  | √ | '' | 扩展表后缀 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdestable | 目标表名 | varchar | 50 |  | √ | ' ' | 目标表名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_migrry_fseq |  | fseq |
| 2 | pk_qcbd_migratentry |  | fentryid |
| 3 | idx_qcbd_migrry_fid |  | fid |

---

## 数据迁移工具_质量云-多语言表 t_qcbd_datamigrat_l

- **表名称：** 数据迁移工具_质量云-多语言表
- **表名：** t_qcbd_datamigrat_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_datamigrat_l |  | fpkid |
| 2 | idx_qcbd_dataatl_fid |  | fid,flocaleid |
| 3 | idx_qcbd_dataatl_fname |  | fname |

---

## 数据迁移工具_质量云-主表 t_qcbd_datamigrat

- **表名称：** 数据迁移工具_质量云-主表
- **表名：** t_qcbd_datamigrat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fisexeinspec | 执行检验单逻辑 | bpchar | 1 |  | √ | '0' | 执行检验单逻辑 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fprefix | fprefix | varchar | 50 |  | √ | ' ' |  |
| 7 | fappvalue | 应用标识 | varchar | 5 |  | √ | ' ' | 应用标识,枚举: qcp :来料 qcpp :生产 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftestbillnos | 测试单据编号 | varchar | 255 |  | √ | ' ' | 测试单据编号 |
| 10 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fissuncess | 数据修复结果 | bpchar | 1 |  | √ | '0' | 数据修复结果 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ferrdesc_tag | 错误描述_详情 | text | 0 |  |  | '' | 错误描述_详情 |
| 15 | fbasedatafield | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 16 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fentitynumberid | 修复主实体对象 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | ferrdesc | 错误描述 | varchar | 255 |  | √ | ' ' | 错误描述 |
| 20 | fupgradestand | 升级标准数据 | bpchar | 1 |  | √ | '0' | 升级标准数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_datamigrat |  | fid |
| 2 | idx_qcbd_dataat_fcreatetime |  | fcreatetime |
| 3 | idx_qcbd_dataat_fnumber |  | fnumber |
