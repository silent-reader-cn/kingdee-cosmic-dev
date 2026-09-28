# 入门必读事项配置-ipop_abc_itemcfg

## 入门必读事项配置-主表 t_ipop_abc_itemcfg

- **表名称：** 入门必读事项配置-主表
- **表名：** t_ipop_abc_itemcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fknowledgeurl | 社区知识链接 | varchar | 200 |  | √ | ' ' | 社区知识链接 |
| 5 | findex | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | flicensegroup | 许可分组/模块 | int8 | 64 |  | √ | 0 | [模块许可分组配置 ipop_init_licgroupcfg](../ipop_files/ipop_init_licgroupcfg.md) |
| 8 | fmoduleid | 所属模块 | int8 | 64 |  | √ | 0 | [入门必读模块配置 ipop_abc_modulecfg](../ipop_files/ipop_abc_modulecfg.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdefault | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 11 | fchecklicense | 是否校验许可 | bpchar | 1 |  | √ | ' ' | 是否校验许可 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_abc_itemcfg_mod |  | fmoduleid |
| 2 | pk_t_ipop_abc_itemcfg |  | fid |
| 3 | idx_ipop_abc_itemcfg_num |  | fnumber |

---

## 入门必读事项配置-多语言表 t_ipop_abc_itemcfg_l

- **表名称：** 入门必读事项配置-多语言表
- **表名：** t_ipop_abc_itemcfg_l

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
| 1 | pk_t_ipop_abc_itemcfg_l |  | fpkid |
| 2 | idx_ipop_abc_itemcfg_l |  | fid,flocaleid |
