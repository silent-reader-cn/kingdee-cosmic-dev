# 页签-mal_tab

## 页签-多语言表 t_mal_tab_l

- **表名称：** 页签-多语言表
- **表名：** t_mal_tab_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_tab_l |  | fpkid |
| 2 | idx_t_mal_tab_l |  | fid,flocaleid |

---

## 页签-主表 t_mal_tab

- **表名称：** 页签-主表
- **表名：** t_mal_tab

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [菜单 mal_menu](../mal_files/mal_menu.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | ftabseq | 页签序号 | int8 | 64 |  | √ | 0 | 页签序号 |
| 6 | fcustplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | flayoutid | 布局 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 9 | fshow_in_login | 登录页显示 | bpchar | 1 |  | √ | '0' | 登录页显示 |
| 10 | ftabnumber | 页签标识 | varchar | 50 |  | √ | ' ' | 页签标识 |
| 11 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fentity | 实体对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_tab |  | fid |
| 2 | idx_mal_tab_ftanseq |  | fnumber |
