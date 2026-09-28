# 解决方案管理-isc_solution_center_m

## 引用资源-子表 t_isc_solution_rr

- **表名称：** 引用资源-子表
- **表名：** t_isc_solution_rr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资源名称 | varchar | 255 |  | √ | ' ' | 资源名称 |
| 3 | ftype | 资源类型 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 4 | fsize | 大小（字节） | int8 | 64 |  | √ | 0 | 大小（字节） |
| 5 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fres_pk | 资源ID | varchar | 50 |  | √ | ' ' | 资源ID |
| 8 | fnumber | 资源编码 | varchar | 255 |  | √ | ' ' | 资源编码 |
| 9 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fres_time | 资源最近修改时间 | timestamp | 0 |  |  | null | 资源最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_solution_rr |  | fentryid |
| 2 | idx_isc_solution_rr |  | fid |

---

## 解决方案管理-多语言表 t_isc_solution_center_l

- **表名称：** 解决方案管理-多语言表
- **表名：** t_isc_solution_center_l

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
| 1 | idx_isc_solution_center_l |  | fid,fname |
| 2 | pk_t_isc_solution_center_l |  | fpkid |

---

## 解决方案管理-主表 t_isc_solution_center

- **表名称：** 解决方案管理-主表
- **表名：** t_isc_solution_center

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkey_words | 关键字 | varchar | 255 |  | √ | ' ' | 关键字 |
| 3 | fgroupid | 方案分类 | int8 | 64 |  | √ | 0 | 解决方案分类 isc_solution_category |
| 4 | flogo | logo | varchar | 255 |  | √ | ' ' | logo |
| 5 | ffreemark | 免费标签图片 | varchar | 5 |  |  | null | 免费标签图片 |
| 6 | foff_shelf_img | 下架标识图片字段 | varchar | 255 |  |  | null | 下架标识图片字段 |
| 7 | fis_store | fis_store | bpchar | 1 |  | √ | '0' |  |
| 8 | ftag | 方案标记 | varchar | 50 |  | √ | 'local' | 方案标记,枚举: local :本地方案包 cloud :云端方案包 |
| 9 | fdomain | 所属领域 | int8 | 64 |  | √ | 0 | 解决方案领域 isc_solution_domain |
| 10 | fconnect_system_name | 连接系统 | varchar | 255 |  | √ | ' ' | 连接系统 |
| 11 | fres_count | 资源数量 | int8 | 64 |  | √ | 0 | 资源数量 |
| 12 | fdetail_tag | 详情_详情 | text | 0 |  |  | null | 详情_详情 |
| 13 | fsource | 开发商 | varchar | 255 |  | √ | ' ' | 开发商 |
| 14 | fispreset | 预置方案 | bpchar | 1 |  | √ | '0' | 预置方案 |
| 15 | fmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 16 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 Z :已下架 |
| 17 | fdetail | 详情 | varchar | 255 |  | √ | ' ' | 详情 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fclicktimes | 浏览次数 | int8 | 64 |  | √ | 0 | 浏览次数 |
| 21 | fisnew | 是否为新 | bpchar | 1 |  | √ | '1' | 是否为新 |
| 22 | fis_deployed | 已部署 | bpchar | 1 |  | √ | '0' | 已部署 |
| 23 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fdeploytimes | 订阅次数 | int8 | 64 |  | √ | 0 | 订阅次数 |
| 28 | fis_update | 是否更新 | bpchar | 1 |  | √ | '0' | 是否更新 |
| 29 | fsize | 资源大小 | varchar | 50 |  | √ | ' ' | 资源大小 |
| 30 | fis_enjoy | 已点赞 | bpchar | 1 |  | √ | '0' | 已点赞 |
| 31 | fintroduction | 简介 | varchar | 255 |  | √ | ' ' | 简介 |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_solution_center |  | fid |
| 2 | idx_isc_solution_center_1 |  | fnumber |

---

## 连接系统(废弃)-多选基础资料表 t_isc_solution_cn

- **表名称：** 连接系统(废弃)-多选基础资料表
- **表名：** t_isc_solution_cn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 连接类型 isc_connection_type |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_solution_cn |  | fpkid |
| 2 | idx_isc_solution_cn |  | fid |

---

## 主资源-子表 t_isc_solution_mr

- **表名称：** 主资源-子表
- **表名：** t_isc_solution_mr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 资源名称 | varchar | 255 |  | √ | ' ' | 资源名称 |
| 4 | ftype | 资源类型 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 5 | fsize | 大小（字节） | int8 | 64 |  | √ | 0 | 大小（字节） |
| 6 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fres_pk | 资源ID | varchar | 50 |  | √ | ' ' | 资源ID |
| 9 | fnumber | 资源编码 | varchar | 255 |  | √ | ' ' | 资源编码 |
| 10 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fres_time | 资源最近修改时间 | timestamp | 0 |  |  | null | 资源最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_solution_mr |  | fentryid |
| 2 | idx_isc_solution_mr_1 |  | fid |
