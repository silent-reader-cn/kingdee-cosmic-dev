# 页面关联单元测试-bos_devp_pageunittest

## 页面关联单元测试-分表 t_bas_unittestdetail_a

- **表名称：** 页面关联单元测试-分表
- **表名：** t_bas_unittestdetail_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fdatasourcename | 导入数据源 | varchar | 36 |  | √ | ' ' | 导入数据源 |
| 3 | fjmxlocation | 测试脚本 | varchar | 100 |  | √ | ' ' | 测试脚本 |
| 4 | fdatasourcecontent | 数据源内容 | text | 0 |  |  | null | 数据源内容 |
| 5 | fprepareindex | 脚本设置 | bpchar | 1 |  | √ | ' ' | 脚本设置,枚举: 0 :进入应用 1 :应用用例 |
| 6 | fjmxcontext | jmx内容 | text | 0 |  |  | null | jmx内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_ut_detail_a_fdsn |  | fdatasourcename |
| 2 | t_bas_unittestdetail_a_pkey |  | fid |

---

## 页面关联单元测试-主表 t_bas_unittestdetail

- **表名称：** 页面关联单元测试-主表
- **表名：** t_bas_unittestdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fparam | 自定义参数 | varchar | 1000 |  |  | null | 自定义参数 |
| 3 | fbizunitid | 应用单元 | varchar | 36 |  |  | null | 应用单元 |
| 4 | fresponser | 负责人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fjmxlocation | fjmxlocation | varchar | 100 |  |  | null |  |
| 6 | fframechose | 测试框架 | bpchar | 1 |  | √ | '0' | 测试框架,枚举: 0 :插件框架 1 :action框架 |
| 7 | flistform | 列表模板 | varchar | 36 |  |  | null | 列表模板 |
| 8 | fresponsers | 负责人 | varchar | 300 |  | √ | ' ' | 负责人 |
| 9 | fdevicetype | 用例平台类型 | bpchar | 1 |  | √ | ' ' | 用例平台类型,枚举: 0 :PC端 1 :移动端 |
| 10 | ftestplugin | 单元测试插件 | varchar | 2000 |  | √ | ' ' | 单元测试插件 |
| 11 | fperpareindex | fperpareindex | varchar | 30 |  |  | null |  |
| 12 | fbizappid | 所属应用 | varchar | 36 |  |  | null | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 13 | fjmxcontext | fjmxcontext | varchar | 255 |  |  | null |  |
| 14 | flevel | 用例级别 | bpchar | 1 |  | √ | '0' | 用例级别,枚举: 0 :0 1 :1 2 :2 |
| 15 | fquerylistnumber | 查询列表编码 | varchar | 30 |  | √ | ' ' | 查询列表编码 |
| 16 | ftype | 发布类型 | varchar | 30 |  |  | null | 发布类型,枚举: 0 :列表 1 :表单 2 :移动列表 3 :移动表单 |
| 17 | fsubsystemid | fsubsystemid | varchar | 32 |  | √ | ' ' |  |
| 18 | freleasetype | 是否发布 | bpchar | 1 |  |  | null | 是否发布 |
| 19 | fobject | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | fnumber | 用例编码 | varchar | 100 |  |  | null | 用例编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_unittestdetail_fnumber |  | fnumber |
| 2 | pk_t_bas_unittestdetail |  | fid |

---

## 页面关联单元测试-多语言表 t_bas_unittestdetail_l

- **表名称：** 页面关联单元测试-多语言表
- **表名：** t_bas_unittestdetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  |  | null |  |
| 2 | fname | 用例名称 | varchar | 100 |  | √ | ' ' | 用例名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_unittestdetail_l_pkey |  | fpkid |
| 2 | idx_bas_unittestdetail_l_fid |  | fid,flocaleid |
