# 检查项-pbd_check_item

## 检查项-主表 t_pbd_checkitem

- **表名称：** 检查项-主表
- **表名：** t_pbd_checkitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [检查项分组 pbd_check_item_group](../pbd_files/pbd_check_item_group.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftype | 检查类型 | bpchar | 1 |  | √ | ' ' | 检查类型,枚举: 1 :指标检查 2 :门槛检查 3 :寻源合规 4 :手工检查 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fdesc | 检查项详细描述 | varchar | 500 |  | √ | ' ' | 检查项详细描述 |
| 15 | fdimid | 检查维度 | int8 | 64 |  | √ | 0 | [分析维度 pbd_dim](../pbd_files/pbd_dim.md) |
| 16 | fpluginname | 插件 | varchar | 255 |  | √ | ' ' | 插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_checkitem |  | fid |
| 2 | idx_pbd_checkitem_fnum |  | fnumber |

---

## 检查项-多语言表 t_pbd_checkitem_l

- **表名称：** 检查项-多语言表
- **表名：** t_pbd_checkitem_l

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
| 1 | idx_pbd_checkitem_l |  | fid,flocaleid |
| 2 | pk_pbd_checkitem_l |  | fpkid |

---

## 单据体-子表 t_pbd_checkitementry

- **表名称：** 单据体-子表
- **表名：** t_pbd_checkitementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | findicatorid | 指标编码 | int8 | 64 |  | √ | 0 | [风险指标 pbd_indicator](../pbd_files/pbd_indicator.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_checkitementry_fid |  | fid |
| 2 | pk_pbd_checkitementry |  | fentryid |

---

## 阈值设置分录-子表 t_pbd_checkitemchkentry

- **表名称：** 阈值设置分录-子表
- **表名：** t_pbd_checkitemchkentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fcheckresultid | 检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 4 | ffiltercondition_tag | 触发条件_详情 | text | 0 |  |  | null | 触发条件_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffiltercondition | 触发条件 | varchar | 1000 |  | √ | ' ' | 触发条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_checkitemchkentry |  | fentryid |
| 2 | idx_pbd_checkitemchkentry_fid |  | fid |
