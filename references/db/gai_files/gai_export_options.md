# 配置导出数据方案-gai_export_options

## 配置导出数据方案-主表 t_gai_export_options2

- **表名称：** 配置导出数据方案-主表
- **表名：** t_gai_export_options2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [Agent功能分组 gai_export_treegroup](../gai_files/gai_export_treegroup.md) |
| 5 | fforeignkey | 关联主对象Id字段 | varchar | 50 |  | √ | ' ' | 关联主对象Id字段 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | findex | 顺序 | int8 | 64 |  | √ | 0 | 顺序 |
| 8 | froutekey | 数据库路由 | varchar | 50 |  | √ | ' ' | 数据库路由 |
| 9 | fllmfields | 模型服务编码字段 | varchar | 50 |  | √ | ' ' | 模型服务编码字段 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fismain | 主业务对象 | bpchar | 1 |  | √ | '0' | 主业务对象 |
| 16 | fbillopenstyle | 单据打开方式 | varchar | 30 |  | √ | ' ' | 单据打开方式,枚举: default :系统默认方式 byplugin :自定义插件 cancel :屏蔽打开 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | ftablename | 实体/表名 | varchar | 50 |  | √ | ' ' | 实体/表名 |
| 19 | fexportmode | 导出方式 | varchar | 50 |  | √ | ' ' | 导出方式,枚举: entity :按实体导出 table :按表导出 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_export_options2 |  | fid |

---

## 配置导出数据方案-多语言表 t_gai_export_options2_l

- **表名称：** 配置导出数据方案-多语言表
- **表名：** t_gai_export_options2_l

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
| 1 | pk_gai_export_options2_l |  | fpkid |

---

## 选择相同Id对象-多选基础资料表 t_gai_export_takeidsto

- **表名称：** 选择相同Id对象-多选基础资料表
- **表名：** t_gai_export_takeidsto

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [配置导出数据方案 gai_export_options](../gai_files/gai_export_options.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_export_takeidsto |  | fpkid |
| 2 | idx_gai_export_takeidsto_fk |  | fid |

---

## 单据体-子表 t_gai_export_optionsentry

- **表名称：** 单据体-子表
- **表名：** t_gai_export_optionsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fexportfield | 预置值字段 | int8 | 64 |  | √ | 0 | [可设置值字段 gai_export_fields](../gai_files/gai_export_fields.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ffieldnames | 字段映射 | varchar | 500 |  | √ | ' ' | 字段映射 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_export_optionsentry |  | fentryid |
