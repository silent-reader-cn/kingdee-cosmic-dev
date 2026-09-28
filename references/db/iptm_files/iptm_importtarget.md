# 目标业务对象列表-iptm_importtarget

## 目标业务对象列表-主表 t_iptm_import_target

- **表名称：** 目标业务对象列表-主表
- **表名：** t_iptm_import_target

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | 目标业务对象列表 iptm_importtarget |
| 5 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 6 | fimportcode | 引入执行码 | varchar | 15 |  | √ | ' ' | 引入执行码 |
| 7 | fentitymeta | 对象编码 | varchar | 80 |  | √ | ' ' | 实体元数据 bos_entitymeta |
| 8 | fmulreplacefield | 数据替换规则的唯一值 | varchar | 50 |  | √ | ' ' | 数据替换规则的唯一值,枚举: |
| 9 | fimportway | 引入方式 | varchar | 50 |  | √ | ' ' | 引入方式,枚举: new :添加新数据 override :更新已有数据 overridenew :更新已有数据并添加新数据 |
| 10 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 11 | ftargetformid | 对象编码 | varchar | 50 |  | √ | ' ' | 对象编码 |
| 12 | forder | 顺序 | int2 | 16 |  | √ | 0 | 顺序 |
| 13 | fcheckgroup | 验证类型 | varchar | 5 |  | √ | ' ' | 验证类型,枚举: 0 :无需验证 1 :许可 2 :特性 |
| 14 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fcloud | 验证简码 | varchar | 20 |  | √ | ' ' | 验证简码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_import_target |  | fid |
| 2 | idx_iptm_targetformid |  | ftargetformid |

---

## 目标业务对象列表-多语言表 t_iptm_import_target_l

- **表名称：** 目标业务对象列表-多语言表
- **表名：** t_iptm_import_target_l

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
| 1 | idx_fid_localeid |  | fid,flocaleid |
| 2 | pk_t_iptm_import_target_l |  | fpkid |
