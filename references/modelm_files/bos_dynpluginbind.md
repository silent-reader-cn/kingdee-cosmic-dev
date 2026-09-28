# 动态插件注册-bos_dynpluginbind

## 动态插件注册-主表 t_meta_dynpluginbind

- **表名称：** 动态插件注册-主表
- **表名：** t_meta_dynpluginbind

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperationkey | 操作代码 | varchar | 36 |  | √ | ' ' | 操作代码 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fdynpluginid | 动态插件 | int8 | 64 |  | √ | 0 | 动态插件定义 bos_dynplugin |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 7 | feffectfields | 影响字段名 | varchar | 255 |  | √ | ' ' | 影响字段名 |
| 8 | fisv | 开发商标识 | varchar | 200 |  | √ | ' ' | 开发商标识 |
| 9 | fapplysubpage | 作用于扩展继承页面 | bpchar | 1 |  | √ | '1' | 作用于扩展继承页面 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fenable | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :可用 |
| 15 | fruncondition_tag | 启用条件json_详情 | text | 0 |  |  | null | 启用条件json_详情 |
| 16 | fruncondition | 启用条件json | varchar | 255 |  |  | ' ' | 启用条件json |
| 17 | fnumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |
| 18 | fobjecttypeid | 页面 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 19 | fclient | fclient | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_dynplubind_dynplu |  | fdynpluginid |
| 2 | idx_meta_dynplubind_optkey |  | foperationkey |
| 3 | pk_meta_dynpluginbind |  | fid |
| 4 | idx_meta_dynplubind_objtype |  | fobjecttypeid |

---

## 动态插件注册-多语言表 t_meta_dynpluginbind_l

- **表名称：** 动态插件注册-多语言表
- **表名：** t_meta_dynpluginbind_l

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
| 1 | idx_meta_dynpluginbind_l_id |  | fid,flocaleid |
| 2 | pk_meta_dynpluginbind_l |  | fpkid |
