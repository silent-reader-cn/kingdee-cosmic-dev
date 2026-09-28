# 组织知识库分组-aikm_xkorg_group

## 组织知识库分组-主表 t_aikm_xkorg_group

- **表名称：** 组织知识库分组-主表
- **表名：** t_aikm_xkorg_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [组织知识库分组 aikm_xkorg_group](../gai_files/aikm_xkorg_group.md) |
| 7 | fvisiblerange | 可见范围 | varchar | 50 |  | √ | ' ' | 可见范围,枚举: public :公开 condition :指定条件 |
| 8 | fvisibleorg | 可见组织 | varchar | 255 |  | √ | ' ' | 可见组织 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fvisiblerole_tag | 可见角色_详情 | text | 0 |  |  | null | 可见角色_详情 |
| 11 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 12 | fvisibleuser | 可见用户 | varchar | 255 |  | √ | ' ' | 可见用户 |
| 13 | fvisibleuser_tag | 可见用户_详情 | text | 0 |  |  | null | 可见用户_详情 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fvisibleorg_tag | 可见组织_详情 | text | 0 |  |  | null | 可见组织_详情 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | feffectivelogic | 生效逻辑 | varchar | 50 |  | √ | ' ' | 生效逻辑 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fvisiblerole | 可见角色 | varchar | 255 |  | √ | ' ' | 可见角色 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aikm_xkorg_group |  | fid |

---

## 组织知识库分组-多语言表 t_aikm_xkorg_group_l

- **表名称：** 组织知识库分组-多语言表
- **表名：** t_aikm_xkorg_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 70 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 70 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aikm_xkorg_group_l |  | fpkid |
| 2 | idx_aikm_xkorg_group_l_0 |  | flocaleid |
