# 辅助资料分类-bos_assistantdatagroup

## 辅助资料分类-主表 t_bas_assistantdata

- **表名称：** 辅助资料分类-主表
- **表名：** t_bas_assistantdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 100000 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fctrlviewid | 组织管控范围 | int8 | 64 |  | √ | 16 | 组织视图方案 bos_org_viewschema |
| 5 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | 辅助资料分类 bos_assistantdatagroup |
| 6 | fsubsystemid | fsubsystemid | varchar | 80 |  |  | ' ' |  |
| 7 | fisgroupcontrol | 集团管控 | bpchar | 1 |  | √ | '0' | 集团管控 |
| 8 | fbizcloudid | 业务云 | varchar | 80 |  |  | null | 业务云 bos_devportal_bizcloud |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 11 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fctrlstrategy | 辅助资料管控策略 | varchar | 10 |  | √ | '6' | 辅助资料管控策略,枚举: 5 :全局共享 7 :私有 6 :资料创建组织范围内共享 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_assistantdata_pkey |  | fid |
| 2 | idx_bas_assistantdata_bizcloud |  | fbizcloudid |
| 3 | idx_bas_assistantdata_parent |  | fparentid |
| 4 | idx_bas_assistantdata |  | fnumber |

---

## 辅助资料分类-多语言表 t_bas_assistantdata_l

- **表名称：** 辅助资料分类-多语言表
- **表名：** t_bas_assistantdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_assistantdata_l |  | flocaleid,fid |
| 2 | t_bas_assistantdata_l_flocaleid_fid_key |  | flocaleid,fid |
| 3 | t_bas_assistantdata_l_pkey |  | fpkid |
