# 数据参数模板-fsa_paramtemplate

## 参数项分录-子表 t_fsa_paramtemplateentry

- **表名称：** 参数项分录-子表
- **表名：** t_fsa_paramtemplateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequesttype | 请求类型 | varchar | 50 |  | √ | ' ' | 请求类型,枚举: 0 :基础资料 1 :请求接口 2 :动态表单 |
| 3 | fdisplay | 是否作为默认显示项 | varchar | 50 |  | √ | ' ' | 是否作为默认显示项,枚举: 0 :否 1 :是 |
| 4 | foperatename | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 5 | fisinput | 是否必录 | bpchar | 1 |  | √ | ' ' | 是否必录 |
| 6 | fparamnumber | 参数编码 | varchar | 30 |  | √ | ' ' | 参数编码 |
| 7 | fcaption | 预览表单名称 | varchar | 50 |  | √ | ' ' | 预览表单名称 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | frelyparamnumber | 依赖参数项编码 | varchar | 50 |  | √ | ' ' | 依赖参数项编码 |
| 10 | fparamdescription | 参数项描述信息 | varchar | 50 |  | √ | ' ' | 参数项描述信息 |
| 11 | fparamname | 参数名称 | varchar | 30 |  | √ | ' ' | 参数名称 |
| 12 | fdefaultvalue | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 13 | ffilter | 过滤标识 | varchar | 50 |  | √ | ' ' | 过滤标识 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fobjecttypeid | 实体对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fformid | 预览表单 | varchar | 50 |  | √ | ' ' | 预览表单 |
| 17 | fdatatype | 数据类型 | bpchar | 1 |  | √ | ' ' | 数据类型,枚举: 0 :日期 1 :基础资料 2 :浮点数 3 :整数 4 :布尔型 5 :字符串 6 :文件上传 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_paramtemplateentry |  | fentryid |
| 2 | idx_fsa_paramtemplateentry |  | fid |

---

## 数据参数模板-主表 t_fsa_paramtemplate

- **表名称：** 数据参数模板-主表
- **表名：** t_fsa_paramtemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [参数分组 fsa_paramgroup](../fsa_files/fsa_paramgroup.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fpluginname | 数据参数处理插件 | varchar | 255 |  | √ | ' ' | 数据参数处理插件 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_paramtemplate |  | fid |
| 2 | idx_fsa_paramtemplate |  | fstatus,fenable,fgroupid |

---

## 数据参数模板-多语言表 t_fsa_paramtemplate_l

- **表名称：** 数据参数模板-多语言表
- **表名：** t_fsa_paramtemplate_l

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
| 1 | pk_t_fsa_paramtemplate_l |  | fpkid |
| 2 | idx_t_fsa_paramtemplate_l |  | fid,flocaleid |
