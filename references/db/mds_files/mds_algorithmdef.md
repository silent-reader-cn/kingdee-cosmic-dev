# 用量概率算法定义-mds_algorithmdef

## 根据目标单据设置-子表 t_mds_algorithmdest

- **表名称：** 根据目标单据设置-子表
- **表名：** t_mds_algorithmdest

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldiddest | 目标字段标识 | varchar | 50 |  | √ | ' ' | 目标字段标识 |
| 3 | fcaldimensiondest | 计算维度 | varchar | 255 |  | √ | ' ' | 计算维度 |
| 4 | fdescribedest | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fcaldimensionvaldest | 计算维度（后台） | varchar | 255 |  | √ | ' ' | 计算维度（后台） |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ffieldnamedest | 目标字段名称 | varchar | 50 |  | √ | ' ' | 目标字段名称 |
| 8 | fcalculatetextdest | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcalculateexcdest | 计算公式（后台） | varchar | 2000 |  | √ | ' ' | 计算公式（后台） |
| 11 | fcalculateexcdest_tag | 计算公式（后台）_详情 | varchar | 2000 |  | √ | ' ' | 计算公式（后台）_详情 |
| 12 | fcalmethoddest | 计算方式 | varchar | 5 |  | √ | ' ' | 计算方式,枚举: 0 :计算公式 1 :插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_algorithmdest |  | fentryid |
| 2 | idx_mds_algorithmdest_id |  | fid |

---

## 用量概率算法定义-主表 t_mds_algorithmdef

- **表名称：** 用量概率算法定义-主表
- **表名：** t_mds_algorithmdef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsrcbill | 来源单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fdestbill | 目标单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_algorithmdef |  | fid |
| 2 | idx_mds_algorithmdef_number |  | fnumber |

---

## 用量概率算法定义-多语言表 t_mds_algorithmdef_l

- **表名称：** 用量概率算法定义-多语言表
- **表名：** t_mds_algorithmdef_l

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
| 1 | pk_mds_algorithmdef_l |  | fpkid |
| 2 | idx_mds_algorithmdef_l_fid |  | fid,flocaleid |

---

## 根据来源单据设置-子表 t_mds_algorithmsrc

- **表名称：** 根据来源单据设置-子表
- **表名：** t_mds_algorithmsrc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcalmethodsrc | 计算方式 | varchar | 5 |  | √ | ' ' | 计算方式,枚举: 0 :计算公式 1 :插件 |
| 3 | fdescribesrc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 4 | ffieldidsrc | 目标字段标识 | varchar | 50 |  | √ | ' ' | 目标字段标识 |
| 5 | fcalculateexcsrc_tag | 计算公式（后台）_详情 | varchar | 2000 |  | √ | ' ' | 计算公式（后台）_详情 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcalculatetextsrc | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 8 | fcaldimensionvalsrc | 计算维度（后台） | varchar | 255 |  | √ | ' ' | 计算维度（后台） |
| 9 | fcaldimensionsrc | 计算维度 | varchar | 255 |  | √ | ' ' | 计算维度 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffieldnamesrc | 目标字段名称 | varchar | 50 |  | √ | ' ' | 目标字段名称 |
| 12 | fcalculateexcsrc | 计算公式（后台） | varchar | 2000 |  | √ | ' ' | 计算公式（后台） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_algorithmsrc |  | fentryid |
| 2 | idx_mds_algorithmsrc_id |  | fid |
