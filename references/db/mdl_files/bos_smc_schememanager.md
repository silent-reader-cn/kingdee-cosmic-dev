# 方案管理-bos_smc_schememanager

## 方案管理-主表 t_meta_schememanager

- **表名称：** 方案管理-主表
- **表名：** t_meta_schememanager

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fassignobject | 分配对象 | varchar | 500 |  |  | ' ' | 分配对象 |
| 3 | fwidgetcontainer | 小部件运行期内容 | text | 0 |  |  | null | 小部件运行期内容 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fschemedesign | 方案 （设计期） | text | 0 |  |  | null | 方案 （设计期） |
| 6 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 应用 |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | ftype | 类型 | varchar | 1 |  | √ | '0' | 类型,枚举: 0 :管理员（出厂预制） 1 :全员（出厂预制） 2 :标准 3 :缺省（出厂预制） |
| 9 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fscene | 场景 | varchar | 1 |  | √ | '0' | 场景,枚举: 0 :首页方案 1 :应用首页方案 |
| 12 | fscheme | 方案 （运行期） | text | 0 |  |  | null | 方案 （运行期） |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_schememanager_pkey |  | fid |
| 2 | idx_kdp_sm_appid |  | fappid |
| 3 | idx_kdp_sm_scene_type |  | ftype,fscene |
| 4 | idx_kdp_sm_num |  | fnumber |

---

## 方案管理-多语言表 t_meta_schememanager_l

- **表名称：** 方案管理-多语言表
- **表名：** t_meta_schememanager_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_schememanager_l_pkey |  | fpkid |
| 2 | idx_kdp_schememanager_localeid |  | fid,flocaleid |
